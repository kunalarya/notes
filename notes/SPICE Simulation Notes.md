---
title: SPICE Simulation Notes
created: '2022-07-06T05:27:17.426Z'
modified: '2022-07-30T00:36:18.622Z'
---

# SPICE Simulation Notes

## Import/export waves

Node label won't match case sensitivity.

## Using custom parts

Need to check pin table matches SUBCKT model.

Ex: 6v6gt
-> Created custom 6v6gt asy
-> Right-click -> View -> Pin Table; ensure the pin labels match the model

In the component dialog
-> SpiceModel: 6V6GT (matches the SUBCKT name, case sensitive)
-> Value: 6v6gt -- case sensitive? Not sure why. Sometimes I need to edit the label itself to get this to work.
