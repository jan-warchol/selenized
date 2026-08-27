;;; selenized-dark-theme.el --- Selenized dark theme -*- lexical-binding: t -*-

;; Copyright (C) 2026 Jan Warchoł

;; Author: Jan Warchoł <jan.warchol@gmail.com>
;; Package-Requires: ((emacs "26.1"))
;; This file is not part of GNU Emacs.

;; This file is free software: you can redistribute it and/or modify
;; it under the terms of the MIT License.

;;; Commentary:

;; Dark variant of the Selenized colour theme.

;;; Code:

(let ((dir (file-name-directory
            (or load-file-name
                (bound-and-true-p byte-compile-current-file)
                buffer-file-name))))
  (add-to-list 'load-path dir))
(require 'selenized)

(deftheme selenized-dark "Selenized dark")

(selenized-create-theme 'dark 'selenized-dark
                        selenized-dark-color-palette-alist)

(provide-theme 'selenized-dark)

;; Local Variables:
;; no-byte-compile: t
;; End:

;;; selenized-dark-theme.el ends here
