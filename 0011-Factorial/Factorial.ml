(** spoj Factorial **)


(*returns the number of trailing
   zeroes at the end of n!*)
let z n =
  (**auxilary funciton that
     acts as a loop**)
  let rec aux q res =
    if q = 0 then res     (**return the result when q = 0**)
    else
      begin
	let q = q / 5 in  (**else divide q by 5**)
	aux q res + q     (**and iterate on q, res+q**)
      end
  in
  aux n 0                 (**execute axuilary function**)
;;


let rec loop i =
  if i > 0 then
    begin
      let n = input_line stdin in
      let n = int_of_string n in
      let out = z n in
      let out = string_of_int out in
      print_endline out;
      loop (i - 1)
    end
;;

loop (int_of_string (input_line stdin))
