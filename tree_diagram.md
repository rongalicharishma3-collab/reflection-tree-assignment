````markdown
```mermaid
q1 --> d1
q1 --> d2
q1 --> q2

d1 --> r1
d2 --> r1
r1 --> q2

q2 --> d3
q2 --> q3
d3 --> r2
r2 --> bridge1
q3 --> bridge1

bridge1 --> q4
q4 --> d4
q4 --> q5
d4 --> r3
r3 --> q5

q5 --> q6
q6 --> bridge2

bridge2 --> q7
q7 --> d5
q7 --> q8
d5 --> r4
r4 --> q8

q8 --> summary
