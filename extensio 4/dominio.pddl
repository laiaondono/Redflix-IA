(define (domain dominioPlanificador)
	(:requirements :typing :adl)
	(:types 
		contenido - object
		dia - object
	)

	(:predicates
	    (predecesor ?c1 - contenido ?c2 - contenido) ;; ?c1 es predecesor de ?c2
   	    (paralelo ?c1 - contenido ?c2 - contenido) ;; ?c1 es paralelo de ?c2
	    (visto ?c - contenido) ;; true si ?c ya ha sido visto por el usuario
	    (pendiente ?c - contenido) ;; true si el usuario tiene pendiente por ver el contenido ?c 
	    (asignado ?c - contenido) ;; true si ?c ha sido asignado al plan
	    (tiene_contenido ?d - dia) ;; true si el ?d tiene un contenido asignado
	    (asignacion ?c - contenido ?d - dia) ;; asignacion del contenido ?c al dia ?d
	    (dia_siguiente ?d1 - dia ?d2 - dia) ;; ?d1 es el dia anterior a ?d2
	)
	(:functions
		(duracion ?c - contenido) ;; duracion del contenido ?c
		(duracionDiaria ?d - dia) ;; duracion de los contenidos vistos en un dia
		(numDia ?d - dia) ;; numero del dia
	)

	(:action asignar_contenido
		:parameters (?c - contenido ?d - dia)	
		:precondition (and  (not (visto ?c))  
							(not (asignado ?c))
							(not (>(+(duracionDiaria ?d) (duracion ?c))200))
							(forall (?c1 - contenido) 
								(and (or  (not (predecesor ?c1 ?c)) 
								   		(and (predecesor ?c ?c1) (pendiente ?c1))
								   		(and (predecesor ?c1 ?c) 
								   			(or (visto ?c1)   
								   				(exists (?d1 - dia)
								   					(and 
								   						(asignacion ?c1 ?d1) 
								   						(<(numDia ?d1) (numDia ?d))
								   					)
								   				)
								   			)
			  				   			)
			  				   		  )
			  				   		(or (not (tiene_contenido ?d))
			  				   			(not (exists (?c2 - contenido) (and (asignacion ?c2 ?d) (predecesor ?c2 ?c1))))
			  				   		)
			  				   )		  				   
							) 
							(forall (?c1 - contenido)  
								(or (and (not (paralelo ?c1 ?c)) (not (paralelo ?c ?c1))) 
									(visto ?c1)
							   		(or (asignacion ?c1 ?d) 
							   		 	(exists (?d1 - dia) (and (asignacion ?c1 ?d1) 
							   		 	(dia_siguiente ?d1 ?d)))
							   		)
							   		(and (not(asignado ?c1))
 						  				 (not (exists (?c2 - contenido) (and (not(asignado ?c2)) (predecesor ?c2 ?c1))))

							   		)

		  				   		)
									  				   
							) 
						)
		:effect (and  (tiene_contenido ?d) (asignado ?c) (asignacion ?c ?d) (increase (duracionDiaria ?d) (duracion ?c)))
	)
)