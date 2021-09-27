def solution(sizes):
    import heapq
    mq_w, mq_h = [], []
    for size in sizes:
        w, h = size[0], size[1]
        if w < h: w, h = h, w
        heapq.heappush(mq_w, -w)
        heapq.heappush(mq_h, -h)
    return mq_w[0] * mq_h[0]