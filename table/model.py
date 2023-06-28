import numpy as np
from PySide2.QtCore import Property, Signal, Slot, QAbstractTableModel
from PySide2.QtQml import QQmlApplicationEngine, qmlRegisterType

class Stats(QAbstractTableModel):
        _data = None # The numbers to calculate over
        _filename = "";

        def __init__(self):
                """ Create the Stats object """
                QAbstractTableModel.__init__(self)

        dataChanged = Signal()

        @Slot()
        def rowCount(self, parent):
                if self._data is None:
                return 0
                return self._data.shape[0]
        
        @Slot()
        def columnCount(self, parent):
                if self._data is None:
                return 0
                return self._data.shape[1]

        @Slot()
        def data(self, index, role):
                if self._data is None:
                return None
                return float(self._data[index.row(),
                                        index.column()])

        dataChanged = Signal()

        @Property(str, notify=dataChanged)
        def filename(self):
                """ The name of the data file """
                return self._filename

        @filename.setter
        def filename(self, name):
                """ Load a new data file """
                self._filename = name
                self.beginResetModel()
                self._data = np.loadtxt(name)
                self.endResetModel()
                self.dataChanged.emit()

        @Property(float, notify=dataChanged)
        def x_mean(self):
                """ The mean of the first column """
                if self._data is None:
                        return 0
                return np.mean(self._data[:, 0])

        @Property(float, notify=dataChanged)
        def y_mean(self):
                """ The mean of the second column """
                if self._data is None:
                        return 0
                return np.mean(self._data[:, 1])

qmlRegisterType(Stats, "Tutorial", 1, 0, "Stats")
