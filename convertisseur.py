import sys

import random

def load_obj(filepath):
    vertices = []
    faces = []
    with open(filepath, 'r') as f:
        for l in f.read().split('\n'):
            if not l.strip() or l[1] != ' ': continue
            if l[0] == 'v':
                vertices.append(l[2:].split(' '))
            elif l[0] == 'f':
#                faces.append(l[2:].split(' ')[0].split('/'))
                faces.append(l[2:].split(' '))
    return vertices, faces

vertices, faces = load_obj(sys.argv[1])
print(len(vertices))
res = [
"""R 400 400
A 0.1 255,255,255
c 0,0,-50 0,0,1 53
l 0,0,-50 0.2 255,255,255
"""
]
for face in faces:
    v1_idx = int(face[0]) - 1
    v2_idx = int(face[1]) - 1
    v3_idx = int(face[2]) - 1
    try:
        v1_pos = vertices[v1_idx]
        v2_pos = vertices[v2_idx]
        v3_pos = vertices[v3_idx]
    except IndexError:
        print('Index Error:', v1_idx, v2_idx, v3_idx)
    res.append(' '.join([
                        'tr',
                        ','.join([v1_pos[0],v1_pos[1],v1_pos[2]]),
                        ','.join([v2_pos[0],v2_pos[1],v2_pos[2]]),
                        ','.join([v3_pos[0],v3_pos[1],v3_pos[2]]),
#                        f'{random.randint(0,255)},{random.randint(0,255)},{random.randint(0,255)}'
                        f'255,255,255'
                    ]))
with open(f'./scenes/{sys.argv[2]}', 'w') as f:
    for l in res:
        f.write(l + '\n')

        
        
