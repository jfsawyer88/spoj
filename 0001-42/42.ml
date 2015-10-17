(** spoj **)
(** Life, the Universe, and Everything **)

let rec loop n =
  if n <> "42" then
    begin
      print_endline n;
      loop (input_line stdin)
    end
;;

loop (input_line stdin)
