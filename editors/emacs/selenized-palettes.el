;;; selenized-palettes.el --- Selenized color palettes -*- lexical-binding: t -*-

;; Copyright (C) 2026 Jan Warchoł

;; Author: Jan Warchoł <jan.warchol@gmail.com>
;; This file is not part of GNU Emacs.

;; This file is free software: you can redistribute it and/or modify
;; it under the terms of the MIT License.

;;; Commentary:

;; Canonical sRGB values from the-values.md.  Dark and light are independent
;; palettes, not one shared gray ramp.

;;; Code:

(defconst selenized-dark-color-palette-alist
  '((bg_0 . "#103c48")
    (bg_1 . "#184956")
    (bg_2 . "#2d5b69")
    (dim_0 . "#72898f")
    (fg_0 . "#adbcbc")
    (fg_1 . "#cad8d9")
    (red . "#fa5750")
    (green . "#75b938")
    (yellow . "#dbb32d")
    (blue . "#4695f7")
    (magenta . "#f275be")
    (cyan . "#41c7b9")
    (orange . "#ed8649")
    (violet . "#af88eb")
    (br_red . "#ff665c")
    (br_green . "#84c747")
    (br_yellow . "#ebc13d")
    (br_blue . "#58a3ff")
    (br_magenta . "#ff84cd")
    (br_cyan . "#53d6c7")
    (br_orange . "#fd9456")
    (br_violet . "#bd96fa"))
  "Selenized dark palette.  Keys are Selenized color names.")

(defconst selenized-light-color-palette-alist
  '((bg_0 . "#fbf3db")
    (bg_1 . "#ece3cc")
    (bg_2 . "#d5cdb6")
    (dim_0 . "#909995")
    (fg_0 . "#53676d")
    (fg_1 . "#3a4d53")
    (red . "#d2212d")
    (green . "#489100")
    (yellow . "#ad8900")
    (blue . "#0072d4")
    (magenta . "#ca4898")
    (cyan . "#009c8f")
    (orange . "#c25d1e")
    (violet . "#8762c6")
    (br_red . "#cc1729")
    (br_green . "#428b00")
    (br_yellow . "#a78300")
    (br_blue . "#006dce")
    (br_magenta . "#c44392")
    (br_cyan . "#00978a")
    (br_orange . "#bc5819")
    (br_violet . "#825dc0"))
  "Selenized light palette.  Keys are Selenized color names.")

(provide 'selenized-palettes)

;;; selenized-palettes.el ends here
