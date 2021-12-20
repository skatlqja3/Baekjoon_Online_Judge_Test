import sys
while True:
    n = list(sys.stdin.readline().strip())
    m_cope = [0] * len(n)
    if int(n[0]) == 0:
        break
    for i in range(len(n)):
        m_cope[i]=n[i]
    m_cope.reverse()
    if n == m_cope:
        print('yes')
    else:
        print('no')