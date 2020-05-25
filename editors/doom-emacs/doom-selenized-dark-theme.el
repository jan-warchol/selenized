;;; doom-selenized-dark-theme -- Dark Selenized Theme for Doom Emacs -*- no-byte-compile: t; -*-
;;; Commentary:

(require 'doom-themes)

;;; Code:
(def-doom-theme doom-selenized-dark
  "Solarized redesigned: fine-tuned color palette for programmers with focus on readability."

  ;; name        default   256       16
  (
    ;; Palette from
    ;; https://github.com/jan-warchol/selenized/blob/master/editors/vim/selenized_black_white.colortemplate
    (blue           '("#4695f7" nil       nil))
    (blue-bright    '("#58a3ff" nil       nil))
    (cyan           '("#41c7b9" nil       nil))
    (cyan-bright    '("#53d6c7" nil       nil))
    (green          '("#75b938" nil       nil))
    (green-bright   '("#84c747" nil       nil))
    (grey0          '("#72898f" nil       nil))
    (grey1          '("#cad8d9" nil       nil))
    (grey2          '("#adbcbc" nil       nil))
    (magenta        '("#f275be" nil       nil))
    (magenta-bright '("#ff84cd" nil       nil))
    (orange         '("#ed8649" nil       nil))
    (orange-bright  '("#fd9456" nil       nil))
    (red            '("#fa5750" nil       nil))
    (red-bright     '("#ff665c" nil       nil))
    (teal0          '("#103c48" nil       nil))
    (teal1          '("#234c57" nil       nil))
    (teal2          '("#2d5b69" nil       nil))
    (violet         '("#af88eb" nil       nil))
    (violet-bright  '("#bd96fa" nil       nil))
    (yellow         '("#dbb32d" nil       nil))
    (yellow-bright  '("#ebc13d" nil       nil))

    ;; Base selenized aliases. From same file.
    (bg0        teal0)
    (bg1        teal1)
    (bg2        teal2)
    (dim0       grey0)
    (fg0        grey2)
    (fg1        grey1)

    ;; Doom variables, aligned with
    ;; https://github.com/jan-warchol/selenized/blob/master/editors/vim/_hl_groups.colortemplate
    (base0      teal0)
    (base1      teal1)
    (base2      teal2)
    (base3      teal2)
    (base4      grey1)
    (base5      grey1)
    (base6      grey1)
    (base7      grey0)
    (base8      grey0)
    (bg         bg0)
    (bg-alt     bg1)
    (fg         fg0)
    (fg-alt     grey2)


    ;; Doom colors
    (grey       grey1)
    (teal       teal2)
    (dark-blue  blue)
    (dark-cyan  cyan)


    ;; face categories -- required for all themes
    (highlight      yellow)
    (selection      orange)

    (error          red)
    (warning        orange)
    (success        green)

    ;; Syntax elements

    (comments       dim0)
    (doc-comments   comments)
    (constants      violet)
    (variables      magenta)
    (strings        cyan)
    (numbers        green-bright)
    (type           green)
    (functions      blue-bright)
    (methods        functions)
    (builtin        functions)
    (keywords       yellow)
    (operators      keywords)

    (vertical-bar   fg1)
    (region         fg1)

    (vc-modified    orange)
    (vc-added       green)
    (vc-deleted     red)

    ;; ;; custom categories
    (hidden     `(,(car bg) "black" "black"))

    (modeline-fg     fg)
    (modeline-fg-alt base5)

    (modeline-bg
        `(,(doom-darken (car bg-alt) 0.15) ,@(cdr base0)))
    (modeline-bg-l
        `(,(doom-darken (car bg-alt) 0.1) ,@(cdr base0)))
    (modeline-bg-inactive   `(,(doom-darken (car bg-alt) 0.1) ,@(cdr bg-alt)))
    (modeline-bg-inactive-l `(,(car bg-alt) ,@(cdr base1))))

    ;; --- extra faces ------------------------
    ((elscreen-tab-other-screen-face :background teal1 :foreground teal0)

    (evil-goggles-default-face :inherit 'region :background (doom-blend region bg 0.5))

    ((line-number &override) :foreground grey0)
    ((line-number-current-line &override) :foreground fg)

    (font-lock-comment-face
     :foreground comments
     :italic italic)
    (font-lock-doc-face
      :inherit 'font-lock-comment-face
      :foreground doc-comments)

    ;; Doom modeline
    (doom-modeline-bar :background highlight)
    (doom-modeline-buffer-file :inherit 'mode-line-buffer-id :weight 'bold)
    (doom-modeline-buffer-path :inherit 'mode-line-emphasis :weight 'bold)
    (doom-modeline-buffer-project-root :foreground green :weight 'bold)

    ;; ivy-mode
    (ivy-current-match :background dark-blue :distant-foreground base0 :weight 'normal)

    ;; --- major-mode faces -------------------
    ;; css-mode / scss-mode
    (css-proprietary-property :foreground orange)
    (css-property             :foreground green)
    (css-selector             :foreground blue)

    ;; LaTeX-mode
    (font-latex-math-face :foreground green)

    ;; markdown-mode
    (markdown-markup-face :foreground base5)
    (markdown-header-face :inherit 'bold :foreground orange)
    ((markdown-code-face &override) :background (doom-lighten bg 0.05))

    ;; org-mode
    (org-hide :foreground hidden)
    (solaire-org-hide-face :foreground hidden))


    ;; --- extra variables ---------------------
    ()
)

(provide 'doom-selenized-dark-theme)
;;; doom-selenized-dark-theme.el ends here
