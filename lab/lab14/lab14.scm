; Lab 14: Final Review

(define (compose-all funcs)
  (if (null? funcs)
    (lambda (x) x)
    (lambda (x) (compose-all (cdr funcs) ((car funcs) x))))
)

(define (has-cycle? s)
  (define (pair-tracker seen-so-far curr)
    (cond ((null? (cdr-stream curr)) #f)
          ((contains? seen-so-far (car curr)) #t)
          (else (pair-tracker (cons (car curr) seen-so-far) (cdr-stream curr))))
    )
  (pair-tracker (list s) s)  ;storaging streams
)

(define (contains? lst s)  ;comparing streams
  (if (null? lst)
    #f 
    (if (equal? s (car lst))
    #t
    (contains? (cdr lst) s)))
)