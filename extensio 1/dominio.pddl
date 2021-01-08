(define (domain dominioPlanificador)
	(:requirements :typing :adl)
	(:types 
		contenido - object
		dia - object
	)

	(:predicates
	    (predecesor ?c1 - contenido ?c2 - contenido) ;; ?c1 es predecesor de ?c2
	    (visto ?c - contenido) ;; true si ?c ya ha sido visto por el usuario
	    (pendiente ?c - contenido) ;; true si el usuario tiene pendiente por ver el contenido ?c 
	    (asignado ?c - contenido) ;; true si ?c ha sido asignado al plan
	    (tiene_contenido ?d - dia) ;; true si el ?d tiene un contenido asignado
	)
	
	(:action asignar_contenido
		:parameters (?c - contenido ?d - dia)	
		:precondition (and  (not (visto ?c)) (not (tiene_contenido ?d)) (not (asignado ?c))
							(forall (?c1 - contenido)  (or (not (predecesor ?c1 ?c)) 
														   (and (predecesor ?c ?c1) (pendiente ?c1))
														   (and (predecesor ?c1 ?c) (or (visto ?c1) (asignado ?c1)))
									  				   )
							) 
						)
		:effect (and  (tiene_contenido ?d) (asignado ?c))
	)
)