[[_TOC_]]
# Prerequisites
## git
### clone
Clones a repository into a newly created directory, creates remote-tracking branches for each branch in the cloned repository (visible using git branch --remotes), and creates and checks out an initial branch that is forked from the cloned repository’s currently active branch.
### add
updates the index using the current content found in the working tree, to prepare the content staged for the next commit.
### commit
Create a new commit containing the current contents of the index and the given log message describing the changes. <br>
Commit z flagą -m dodaje wiadomość np. *git commit -m "feat: create new line of code"*
### push (--force)
Wypycha zmiany z lokalnego repozytorium do zdalnego (remote).<br>
*git push origin main*
### checkout (-b)
przełączanie na inny branch lub tworzenie nowego brancha. Z flagą -b tworzy i od razu przełącza na tworzonego brancha.
### pull
uaktualnia repo np. *git pull origin dev*, gdzie dev to nazwa brancha
### branch
informacja, na którym branchu aktualnie jesteśmy, możemy wylistowac branche z flagą --list (chyba)
### merge
Incorporates changes from the named commits (since the time their histories diverged from the current branch) into the current branch. This command is used by git pull to incorporate changes from another repository and can be used by hand to merge changes from one branch into another.<br><br>
Jeśli chcemy domergować zmiany np. z deva do naszego brancha to będąc na naszym branchu wpisujemy komendę *git branch dev*<br>
https://www.atlassian.com/git/tutorials/using-branches/git-merge
### rebase
tworzy liniową strukturę commitów, brak historii<br>
https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase

### reset
git-reset - Reset current HEAD to the specified state
### clean
Cleans the working tree by recursively removing files that are not under version control, starting from the current directory.
### diff
Show changes between commits, commit and working tree, etc
### status
pokazuje pliki w lokalnym repo (śledzone, nieśledzone, czy coś jest do zacommitowania)
## GitHub
## markdown
## edytor
### vi, vim, emacs (do pracy z konsoli)
### PyCharm, VSCode (do pracy z GUI)
## komendy bashowe i ich flagi
### cd
zmiana directory np. cd home/
### ls
wypisuje wszystkie pliki w danej lokalizacji, z flagą -a listuje również te ukryte.
### pwd
aktualne working directory
### echo
Wyświetlanie tekstu ze standardowego wejścia (klawiatura).
### touch
aktualizacja/modyfikacja daty ostatniego zapisu pliku lub tworzy nowy plik 
### mkdir
tworzenie nowego katalogu
### grep
filtrowanie danych wg jakiegoś klucza
### man
manual - podręcznik np. *man ls* wypisze podręcznik do polecenia ls
### cp
copy - kopiuje pliki i katalogi<br>

    $ cp [opcje] [-T] źródło cel

    $ cp [opcje] źródło katalog

    $ cp [opcje] -t katalog źródło 
### mv
move - przenosi plik
### rmdir
remove directory
### rm
remove file
### cat
wyświetlanie zawartości pliku
### less, more
less – program konsoli Uniksa, wyświetlający duże ilości tekstu w sposób przystępny dla użytkownika (tzw. pager). W odróżnieniu od more zezwala na nawigację po pliku w obu kierunkach w dowolnym momencie. W przeciwieństwie do vi, który także może być używany do wyświetlania plików, less nie wczytuje całego pliku przy starcie, dzięki czemu szybciej wczytuje duże pliki. 
### head, tail
### ps
wyświetla listę procesów
### kill
ubija proces, polecenie kill potrzebuje chyba numeru procesu, w przeciwieństwie do sigkill???
### xargs (to trudne)
### ssh
secure shell - bezpieczny sposób połączenia z użyciem kluczy prywatnego oraz publicznego
### > (przekierowanie stdout np do pliku)
echo "some text here" > /path/to/file<br>nadpisuje cały plik, jeśli istnieje<br><br>
echo "Some text to be appended" >> /path/to/file<br>
dodaje output na koniec tekstu, jeśli plik istnieje
### /dev/null
### | (pipe, przekierowanie wyniku do kolejnego polecenia)
### chmod
### exit