;;; selenized-light-theme.el --- Selenized light theme -*- lexical-binding: t -*-

;; Copyright (C) 2026 Jan Warchoł

;; Author: Jan Warchoł <jan.warchol@gmail.com>
;; Package-Requires: ((emacs "26.1"))
;; This file is not part of GNU Emacs.

;; This file is free software: you can redistribute it and/or modify
;; it under the terms of the MIT License.

;;; Commentary:

;; Light variant of the Selenized colour theme.

;;; Code:

(let ((dir (file-name-directory
            (or load-file-name
                (bound-and-true-p byte-compile-current-file)
                buffer-file-name))))
  (add-to-list 'load-path dir))
(require 'selenized)

(deftheme selenized-light "Selenized light")

(selenized-create-theme 'light 'selenized-light
                        selenized-light-color-palette-alist)

(provide-theme 'selenized-light)

;; Local Variables:
;; no-byte-compile: t
;; End:

;;; selenized-light-theme.el ends here
