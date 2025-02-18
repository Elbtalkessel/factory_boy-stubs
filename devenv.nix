_: {
  languages = {
    python = {
      enable = true;
      venv = {
        enable = true;
        requirements = ''
          setuptools
          mypy
          factory_boy
        '';
      };
    };
  };

  git-hooks.hooks = {
    trim-trailing-whitespace.enable = true;
    autoflake.enable = true;
    black.enable = true;
    check-python.enable = true;
    end-of-file-fixer.enable = true;
    flake8.enable = true;
    isort.enable = true;
    mixed-line-endings.enable = true;
    ruff.enable = true;
    ruff-format.enable = true;
  };

  scripts = {
    makestubs.exec = ''
      stubgen --export-less -p factory -o .
      rm -rf factory-stubs 2>/dev/null
      mv factory factory-stubs
    '';
  };
}
