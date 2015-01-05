Project Gate: system for unlocking doors using RFID cards
---------------------------------------------------------

This project aims to create a system for our university that will allow ISICs or
ITICs to be used for accessing doors. We will provide a complete system for
managing access rules (integrated with the university's electronic info system),
and the embedded devices hardware and software.

This repository contains several separate subprojects in branches:
- [`server/master`](https://github.com/fmfi-svt/gate/tree/server/master): the server (DB, "manager")
- [`controller-sw/master`](https://github.com/fmfi-svt/gate/tree/controller-sw/master): the
  controller's software (decide whether to open this door)
- [`controller-hw/master`](https://github.com/fmfi-svt/gate/tree/controller-hw/master): the
  controller's hardware design
- [`reader-sw/master`](https://github.com/fmfi-svt/gate/tree/reader-sw/master): the reader's
  software (read ISIC, tell it to the
  controller)
- [`reader-hw/master`](https://github.com/fmfi-svt/gate/tree/reader-hw/master): the reader's
  hardware design

See the [Architecture](https://github.com/fmfi-svt/gate/wiki/Architecture) wiki page for
more details about what is what.

The recommended way to work with this repo structure is to checkout a separate
clone for every subproject.
