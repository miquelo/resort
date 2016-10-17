TODO
====

Version 0.3
-----------

* Desapareix el cocepte "contextual".
* Desapareixen les comandes "insert" i "delete". Es manté "update".
* Els components s'activen o desactiven mitjançant configuració de perfil, en la
  secció "enabled" del fitxer "profile.ini": component_name = (true|false).
* Cada component té un estat, detector del qual és retornat per
  "Profile.state(comp_name)", que determina si s'ha canviat l'estat en el codi
  font (local o remot).
  - ComponentState.changed()
* La comanda "update" actualitza els components en funció dels canvis d'estat i
  si estan activats o desactivats.
* El "work_dir" passa a ser "profiles_dir". Ara el "work_dir", que és el
  directori de treball dels components, és el directori "work" dins de
  "profile_dir".
  Dins de "profile_dir" està el directori "state", on es manté l'últim indicador
  d'estat. Així doncs, l'estructura de fitxers dins de "profile_dir" és:
  - state/
  - work/
  - profile.ini
* LocalGitComponentState. Comprova si ha canviat l'estat dels directoris
  indicats mitjançant una operació equivalent a "git status \<directoris\>".
  - http://gitpython.readthedocs.io/en/stable/index.html
  - http://stackoverflow.com/questions/17224134/check-status-of-local-python-relative-to-remote-with-gitpython
  
  En un fitxer del directori "state" es manté el hash de l'últim commit, que es
  sobreescriu al final de cada consulta de l'estat. L'estat es considera canviat
  quan no hi ha fitxer de hash d'últim commit, o bé quan el commit actual té un
  hash diferent del que hi ha en aquest fitxer.

BÁSICO-2
--------

* ComponentTask returned by Component.insert(context) and
  Component.delete(context). Task is executed by ComponentTask.execute(work)
  method, and cancelled by ComponentTask.cancel() method.

