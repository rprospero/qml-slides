import QtQuick 2.12
import QtQuick.Controls 2.15
import QtQuick.Dialogs 1.3
import QtQuick.Layouts 1.2
import Tutorial 1.0

Rectangle {
  width: 600
  height: 600
  color: "#F0F0F0"

  Stats {
    id: myStats
    filename: "file:data.txt"
  }

  FileDialog {
    id: fileDialog
    title: "Choose a data file"
    onAccepted: myStats.filename = fileDialog.fileUrl
  }

  Text {
    id: titleText
    text: "Stat Calculator"
    anchors.top: parent.top
    anchors.horizontalCenter: parent.horizontalCenter
  }

  Button {
          id: loadButton
          anchors.top: titleText.bottom
          anchors.left: parent.left
          anchors.right: parent.right
          text: "Load file"
          onClicked: fileDialog.open()
  }

  TableView {
          anchors.top: loadButton.bottom
          anchors.bottom: parent.bottom
          anchors.left: parent.left
          width: parent.width
          model: myStats
          columnSpacing:10
  
          delegate: Rectangle {
                  color: "#F0F0F0"
                  implicitWidth: 280
                  implicitHeight: realText.height + 5
                  Text {
                          id: realText
                          text: display
                  }
          }
  }
}