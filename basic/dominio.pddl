(define (domain dominioPlanificador)
    (:requirements :adl :typing :fluents)
    (:types 
        contenido - object
        dia - object
    )
    (:predicates
        (predecesor ?c1 - contenido ?c2 - contenido) ;; ?c1 es predecesor de ?c2
        (visto ?c1 - contenido) ;; true si ?c1 ya ha sido visto por el usuario
        (asignado ?c1 - contenido) ;; true si ?c1 ha sido asignado al plan
        (pendiente ?c1 - contenido) ;; true si ?c1 ha sido asignado al plan
        (tiene_contenido ?d - dia) ;; true si el ?d tiene un contenido asignado
    )

    (:action asignar-contenido
        :parameters (?c - contenido ?d - dia)
        :precondition   (and  
                            (not (visto ?c)) 
                            (not (tiene_contenido ?d)) 
                            (not (asignado ?c)) 
                            (not (exists (?c1 - contenido) (and (not(visto ?c1)) (not(asignado ?c1)) (predecesor ?c1 ?c))))
                        )
        :effect (and (asignado ?c) (tiene_contenido ?d))
    )


)
