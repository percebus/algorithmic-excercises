# algorithmic-excercises

## TODOs

- [ ] `mypy --strict` for all `.py` files
- [ ] Centralize print("✅") in `lib`
- [ ] Remove `src.` from all `import`s
- [ ] Remove `python` commands from `package.json`.

### CLI cmds

Move CLI cmds like `pypyr` to `requirements.pipx.txt`

- [ ] `mypy`: There is another `mypy-extensions` dependency
- [ ] `ruff`: `pypyr lint` did NOT work
- [ ] `pylint`: `pypyr lint` did NOT work
- [ ] `pyright`: `pypyr lint` did NOT work
- [ ] etc.

## Done

- [x] ~~Remove `tests/` from `coverage`~~
- [x] ~~Rename `requirements.min.txt` to `requirements.main.txt`, to hint that it comes from `poetry` `main` dependencies.~~

### requirements.pipx.txt

Move CLI cmds like `pypyr` to `requirements.pipx.txt`

- [x] ~~`flake8`~~
- [x] ~~`pre-commit`~~
- [x] ~~`pyclean`~~
- [x] ~~`pypyr`~~
