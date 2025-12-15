_MISSING = object()

def dig(obj, path, default=None):
    cur = obj
    for key in path:
        try:
            if isinstance(cur, dict):
                cur = cur.get(key, _MISSING)
            else:
                cur = cur[key]  # list/tuple (and also dict fallback if you pass non-dict)
        except (KeyError, IndexError, TypeError):
            return default

        if cur is _MISSING:
            return default

    return cur