teaches_course(f1,calculus).

teaches_course(f2,linear_algebra).

teaches_course(f3,dsa).

teaches_course(f4,dsa).


teaches_course(f5,ppl).

teaches_course(f6,ppl).

teaches_course(f7,dld).

teaches_course(f8,dtl).

 

has_course(math_dept,calculus).

has_course(math_dept,linear_algebra).

has_course(comp_dept,dsa).

has_course(comp_dept,ppl).

has_course(comp_dept,dtl).

has_course(comp_dept,dld).



has_student(comp_dept,s1).

has_student(comp_dept,s2).

has_student(math_dept,s3).

 

faculty_at(F,D) :- teaches_course(F,C) , has_course(D,C).

studies_course(S,C) :- has_student(D,S) , has_course(D,C).

studies_under(S,F):- has_course(D,C) , has_student(D,S) , teaches_course(F,C).