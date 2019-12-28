# https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa

def choose_best_sum(t, k, ls):
    results = {}
    def loop(t, k, ls):
        key = (t, tuple(ls))
        if key in results:
            return results[key]
        if len(ls) < k:
            result = None
        elif k == 0:
            result = 0
        else:
            candidate = []
            for i, l in enumerate(ls):
                if l <= t:
                    tmp = loop(t-l, k-1, ls[:i] + ls[i+1:])
                    if not tmp is None:
                        candidate.append(tmp + l)
            if candidate:
                result = max(candidate)
            else:
                result = None
        results[key] = result
        return result
    return loop(t, k, ls)