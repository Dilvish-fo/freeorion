# Handlers allow to add debug features to AI with out modifying existing code.

## Attach handler

  - create python file
  - add call of `register_pre_handler` or `register_post_handler`
  - add handler to config file (section: `main`, key: `handler` space separated names of python files with out extension)
  - run game with config file

## Existing handlers:
  - `charts_handler`:
    Debug prints required for charts. Started by default
  - `inspect_freeOrionAIInterface`:
    Code that create stub for `freeOrionAIInterface`. Must be launched with single AI player.
