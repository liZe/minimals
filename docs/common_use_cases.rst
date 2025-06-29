Common Use Cases
================


Play the Game
-------------

The main feature of the current version of the game is to display a customized "Hello" message::

  $ minimals pykachu
  Hello, I am mini-pykachu!

It works well with many names! You can try::

  $ minimals mewpythontwo
  Hello, I am mini-mewpythontwo!
  $ minimals bulpyzarre
  Hello, I am mini-bulpyzarre!


Create your own Game
--------------------

Minimals can be used to build your own game::

  from minimals import hello

  name = input("Which Minimal do you want? ")
  print(hello(name))
