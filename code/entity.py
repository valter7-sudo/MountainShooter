#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABC


class Entity(ABC):

	def __init__(self):
		self.name: str = None
		self.surf: Surface = None
		self.rect: Rect = None

	def move(self) -> -> None:
		pass
