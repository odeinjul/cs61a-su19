(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))



;; Problem 17
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 17
  'replace-this-line
  (define (helper index s)
    (if (equal? nil s)
      nil
      (if (equal? nil (cdr s))
      (cons (cons index (cons (car s) nil)) nil)
      (cons (cons index (cons (car s) nil)) (helper (+ index 1) (cdr s)))
    ))
  )
  (helper 0 s)
)
  ; END PROBLEM 17

;; Problem 18

(define (zip pairs)
  ; BEGIN PROBLEM 18
  ;'replace-this-line
  ;(define (cadar s)
  ;  (car (cdr (car s))))
  ;(define (helperx pairs x)
  ;  (print x)
  ;  (if (equal? nil (cdr pairs))
  ;    (cons x (cons (caar pairs) nil))
  ;    (helperx (cdr pairs) (cons x (cons (caar pairs) nil)))))
  ;(define (helpery pairs x)
  ;  (print x)
  ;  (if (equal? nil (cdr pairs))
  ;    (cons x (cons (cadar pairs) nil))
  ;    (helpery (cdr pairs) (cons x (cons (cadar pairs) nil)))))
  ;(if (equal? nil pairs)
  ;  (list nil nil)
  ;  (list (helperx (cdr pairs) (caar pairs)) (helpery (cdr pairs) (cadar pairs))))
  ;)
  (list (map car pairs) (map cadr pairs)))
  ; END PROBLEM 18


;; Problem 19
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 19
          expr
         ; END PROBLEM 19
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr)) ;'lambda' / 'define'
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           (cons form (cons params (map let-to-lambda body)))
           ; END PROBLEM 19
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           (append (cons (cons 'lambda (cons (car (zip values)) (map let-to-lambda body))) nil) (map let-to-lambda (cadr (zip values))))
           ; END PROBLEM 19
           ))
        (else
         ; BEGIN PROBLEM 19
         (cons (car expr) (map let-to-lambda (cdr expr)))
         ; END PROBLEM 19
         )))
