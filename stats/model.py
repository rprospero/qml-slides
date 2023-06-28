import numpy as np
from PySide2.QtCore import QObject, Property
from PySide2.QtQml import QQmlApplicationEngine, qmlRegisterType
class Stats(QObject):
  _data = None
  def __init__(self):
	QObject.__init__(self)
	self.data_ = np.loadtxt("data.txt")
  @Property(float)
  def x_mean(self):
	return np.mean(self.data_[:, 0])
  @Property(float)
  def y_mean(self):
	return np.mean(self.data_[:, 1])
qmlRegisterType(Stats, "Tutorial", 1, 0, "Stats")
