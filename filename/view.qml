import QtQuick 2.0
import QtQuick.Layouts 1.2
import Tutorial 1.0

Rectangle {
  width: 600
  height: 600
  color: "#F0F0F0"

  Stats {
    id: myStats
    filename: "data.txt"
  }

  Text {
    id: titleText
    text: "Stat Calculator"
    anchors.top: parent.top
    anchors.horizontalCenter: parent.horizontalCenter
  }

  GridLayout {
    anchors.top: titleText.bottom
    anchors.bottom: parent.bottom
    anchors.left: parent.left
    anchors.right: parent.right
  
    columns: 2
  
    Text {text: "X mean"}
    Text {text: myStats.x_mean}
    Text {text: "Y mean"}
    Text {text: myStats.y_mean}
  }
}
