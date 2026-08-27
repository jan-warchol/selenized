;;; selenized.el --- Selenized theme infrastructure -*- lexical-binding: t -*-

;; Copyright (C) 2026 Jan Warchoł

;; Author: Jan Warchoł <jan.warchol@gmail.com>
;; Keywords: faces
;; Package-Requires: ((emacs "26.1"))
;; URL: https://github.com/jan-warchol/selenized
;; This file is not part of GNU Emacs.

;; This file is free software: you can redistribute it and/or modify
;; it under the terms of the MIT License.

;;; Commentary:

;; Shared machinery for the Selenized dark and light Emacs themes.
;; Load a variant with `load-theme':
;;
;;   (load-theme 'selenized-dark t)
;;   (load-theme 'selenized-light t)
;;
;; `selenized-toggle-theme' switches between those two.

;;; Code:

(eval-and-compile
  (let ((dir (file-name-directory
              (or load-file-name
                  (bound-and-true-p byte-compile-current-file)
                  buffer-file-name))))
    (when dir
      (add-to-list 'load-path dir))))

(require 'selenized-palettes)
(require 'selenized-faces)

(defgroup selenized nil
  "Selenized color theme."
  :group 'faces)

(defconst selenized-themes '(selenized-dark selenized-light)
  "Bundled Selenized theme variants.")

(defun selenized-create-theme (variant theme-name palette)
  "Define THEME-NAME of VARIANT using PALETTE.

VARIANT is `dark' or `light'.  PALETTE is an alist of Selenized
color names to sRGB hex strings."
  (apply #'custom-theme-set-faces
         theme-name
         (selenized-face-specs palette))
  (apply #'custom-theme-set-variables
         theme-name
         (selenized-variable-specs palette variant)))

;;;###autoload
(defun selenized-toggle-theme ()
  "Toggle between `selenized-dark' and `selenized-light'."
  (interactive)
  (let ((next (if (memq 'selenized-dark custom-enabled-themes)
                  'selenized-light
                'selenized-dark)))
    (mapc #'disable-theme selenized-themes)
    (load-theme next t)))

;;;###autoload
(when (and (boundp 'custom-theme-load-path) load-file-name)
  (add-to-list 'custom-theme-load-path
               (file-name-as-directory (file-name-directory load-file-name))))

(provide 'selenized)

;;; selenized.el ends here
