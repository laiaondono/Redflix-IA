(define (problem problemaPlanificador) 
  (:domain dominioPlanificador)
  
  (:objects
     c1 c2 c3 c4 c5 c6 c7 - contenido
    dia1 dia2 dia3 dia4 dia5 dia6 dia7 - dia
  )

  (:init
    (predecesor c4 c6)
    (predecesor c2 c3)
    (predecesor c3 c4)
    (predecesor c1 c5)
    (predecesor c7 c1)
    (paralelo c6 c7)
    (visto c2)
    (pendiente c3)
    (pendiente c5)
    (pendiente c6)
    (dia_siguiente dia1 dia2)
    (dia_siguiente dia2 dia3)
    (dia_siguiente dia3 dia4)
    (dia_siguiente dia4 dia5)
    (dia_siguiente dia5 dia6)
    (dia_siguiente dia6 dia7)
  ) 

  (:goal (and (asignado c3) (asignado c5) (asignado c6))
  )
)

;;         c7 c1 c5
;;c2 c3 c4 c6