import QtQuick 2.0
import Tutorial 1.0

Rectangle {
  width: 200
  height: 200
  color: "#F0F0F0"
  Stats {id: myStats;}
  Text {
	text: myStats.x_mean + ", " + myStats.y_mean
	anchors.centerIn: parent
  }
}
