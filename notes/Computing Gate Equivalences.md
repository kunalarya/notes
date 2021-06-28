---
title: Computing Gate Equivalences
created: '2020-12-19T19:59:23.619Z'
modified: '2020-12-19T19:59:29.861Z'
---

# Computing Gate Equivalences

Show the following:
```
q0 --[X]--o-------
          |
q1 -------Z-------
```
is equivalent to
```
q0 -------o--[X]--
          |
q1 -------Z--[Z]--
```

That is, if you push an $X$ gate through the control for a $CZ$ gate, it is equivalent to adding a phase ($Z$) on the target qubit.

Let's use numpy to see if we can infer this.





