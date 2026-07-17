
import sqlite3, json, sys
from pathlib import Path
from datetime import datetime, timezone

DB_PATH = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(r"C:\Users\Marco\AppData\Local\Microsoft\Edge\User Data\Default\Collections\collectionsSQLite")
OUT_PATH = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("edge-collections-lite-backup-compatible.json")


def iso_from_edge_ts(value):
    if value in (None, ''):
        return None
    try:
        v = float(value)
    except Exception:
        return None
    if v > 1e12:
        v /= 1000.0
    return datetime.fromtimestamp(v, tz=timezone.utc).isoformat()


def decode_blob_json(blob):
    if blob is None:
        return None
    if isinstance(blob, memoryview):
        blob = bytes(blob)
    if isinstance(blob, bytes):
        try:
            return json.loads(blob.decode('utf-8'))
        except Exception:
            try:
                return json.loads(blob.decode('utf-8', errors='ignore'))
            except Exception:
                return None
    return None


def extract_source(blob):
    obj = decode_blob_json(blob) or {}
    return obj.get('url') or '', obj.get('websiteName') or ''


def main():
    if not DB_PATH.exists():
        raise SystemExit(f"Database non trovato: {DB_PATH}")
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    collections = {}
    for row in cur.execute('SELECT * FROM collections ORDER BY position ASC, date_created ASC'):
        collections[row['id']] = {
            'id': row['id'],
            'title': row['title'] or 'Senza titolo',
            'createdAt': iso_from_edge_ts(row['date_created']),
            'updatedAt': iso_from_edge_ts(row['date_modified']),
            'notes': [],
            'items': []
        }

    sql = (
        'SELECT r.parent_id, i.id, i.date_created, i.date_modified, i.title, i.source, '
        'i.favicon_url, i.canonical_image_url, i.text_content, i.html_content, i.type, i.remote_url '
        'FROM collections_items_relationship r '
        'JOIN items i ON i.id = r.item_id '
        'ORDER BY r.parent_id, r.position ASC'
    )

    for row in cur.execute(sql):
        source_url, website_name = extract_source(row['source'])
        canonical_image_url = row['canonical_image_url'] or ''
        final_url = source_url or row['remote_url'] or ''
        item_type = 'page' if (row['type'] or '').lower() == 'website' else (row['type'] or 'page')
        item = {
            'id': row['id'],
            'addedAt': iso_from_edge_ts(row['date_created']),
            'updatedAt': iso_from_edge_ts(row['date_modified']),
            'type': item_type,
            'title': row['title'] or final_url or 'Senza titolo',
            'url': final_url,
            'sourceUrl': final_url,
            'websiteName': website_name,
            'text': row['text_content'] or '',
            'htmlContent': row['html_content'] or '',
            'imageUrl': canonical_image_url,
            'canonicalImageUrl': canonical_image_url,
            'screenshotUrl': '',
            'favicon': row['favicon_url'] or ''
        }
        parent = collections.get(row['parent_id'])
        if parent:
            parent['items'].append(item)

    result = {
        'app': 'Collections Replica',
        'version': '1.3.0-lite',
        'exportedFrom': 'Microsoft Edge collectionsSQLite',
        'exportedAt': datetime.now(timezone.utc).isoformat(),
        'data': {
            'collections': list(collections.values()),
            'settings': {'lastCollectionId': next(iter(collections.keys()), None)}
        }
    }
    OUT_PATH.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
    print(OUT_PATH)
    print(f"collections={len(result['data']['collections'])}")
    print(f"items={sum(len(c['items']) for c in result['data']['collections'])}")


if __name__ == '__main__':
    main()
