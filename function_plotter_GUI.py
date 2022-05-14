

from PyQt5.QtCore import QCoreApplication, QSize, Qt, QMetaObject
from PyQt5.QtWidgets import *
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np


class DisplayFunctionPlot(FigureCanvas):
    """"
    Display Function Plot figure object
    :cvar
    """

    def __init__(self):
        # create figure , axes
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot()
        super().__init__(self.fig)

        # set styles to the figure
        self.set_style()

    def set_style(self):
        """
        set style to the figure, axes
        :cvar
        """
        # Configure the grid lines displayed on the map with the labels on x amd y.
        plt.grid(True, color='w', linestyle="dotted", alpha=0.3, linewidth=1)

        # set color of labels on x,y , figure , axes
        self.ax.set_facecolor('#303030')
        self.fig.patch.set_facecolor('#303030')
        self.ax.xaxis.label.set_color('#bfbfbf')
        self.ax.yaxis.label.set_color('#bfbfbf')

        # set spines' color
        self.ax.spines['bottom'].set_color('#bfbfbf')
        self.ax.spines['top'].set_color('#bfbfbf')
        self.ax.spines['right'].set_color('#bfbfbf')
        self.ax.spines['left'].set_color('#bfbfbf')

        # set spins opacity
        self.ax.spines['bottom'].set_alpha(0.2)
        self.ax.spines['top'].set_alpha(0.2)
        self.ax.spines['right'].set_alpha(0.2)
        self.ax.spines['left'].set_alpha(0.2)

        # set ticks color
        plt.yticks(color='#F0F0F0')
        plt.xticks(color='#F0F0F0')

        # tight figure to the display size
        plt.tight_layout()


def validate_input(input_object, massage=None):
    """
        flag error (change color of input field in case of wrong data or empty fields )
        :parameter: input_object the input field changed
    """
    # change StyleSheet to error style (red color)
    input_object.setStyleSheet("""
                                QLineEdit{
                                                border:1px solid #b01e0b;
                                                background-color: rgba(176, 30, 11, 0.1);
                                                font-family: Segoe ui;
                                                font-style: normal;
                                                font-weight: normal;
                                                font-size: 15px;
                                                line-height: 14px;
                                                border-radius:10px;
                                                color: rgb(191, 191, 191);
                                            } 

                                            QLineEdit:hover{
                                                background-color: rgb(68, 68, 68);
                                """)
    input_object.clear()

    # change PlaceholderText to the error message
    if massage:
        input_object.setPlaceholderText(massage)
    else:
        input_object.setPlaceholderText("Required Field")


def refactor_style(input_object):
    """
        return input fields to there original case
        :parameter: input_object the input field changed
    """
    # return input to original style
    input_object.setStyleSheet("""
                QLineEdit{
                border:none;
                background-color: rgb(63, 63, 63);
                font-style: normal;
                font-weight: normal;
                font-size: 15px;
                line-height: 14px;
                border-radius:10px;
                color: rgb(191, 191, 191);
                padding-left:5px;
            } 
            
            QLineEdit:hover{
                background-color: rgb(68, 68, 68);
            }
                """)

    if input_object.objectName() == "function_input":
        input_object.setPlaceholderText("Enter a Function to plot")

    elif input_object.objectName() == "minimum_input":
        input_object.setPlaceholderText("Value to start from")

    elif input_object.objectName() == "maximum_input":
        input_object.setPlaceholderText("Value to end at")


class FunctionPlotter(QMainWindow):
    """
    application to plot mathematical function
    """
    def __init__(self):
        super(FunctionPlotter, self).__init__()

        # main frames
        self.central_widget = QWidget(self)
        self.central_widget_grid = QGridLayout(self.central_widget)
        self.main_holder = QFrame(self.central_widget)
        self.main_holder_grid = QGridLayout(self.main_holder)

        # plots display frame
        self.plotting_frame = QFrame(self.main_holder)
        self.plotting_frame_grid = QGridLayout(self.plotting_frame)
        self.display_function_plot = DisplayFunctionPlot()

        # inputs holder area
        self.inputs_group_box = QGroupBox(self.main_holder)
        self.inputs_group_box_grid = QGridLayout(self.inputs_group_box)

        # function input
        self.function_label = QLabel(self.inputs_group_box)
        self.function_input = QLineEdit(self.inputs_group_box)

        # maximum input
        self.maximum_label = QLabel(self.inputs_group_box)
        self.maximum_input = QLineEdit(self.inputs_group_box)

        # minimum input
        self.minimum_input = QLineEdit(self.inputs_group_box)
        self.minimum_label = QLabel(self.inputs_group_box)

        # submit button
        self.plot_button = QPushButton(self.inputs_group_box)

        self.inputs_grid = QGridLayout()
        self.inputs_layout = QVBoxLayout()
        self.labels_layout = QVBoxLayout()
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.set_features()
        self.set_text()
        self.set_style()
        self.set_actions()

    def set_style(self):
        """
        function to set StyleSheet for the application
        """
        self.central_widget.setStyleSheet("""
                QWidget{
                    background-color: rgb(38, 38, 38);
                }
                
                QGroupBox{
                    border: 2px solid #3f3f3f;
                    border-radius:6px;
                    background-color: rgb(48, 48, 48);
                }
                
                QGroupBox::title {
                    padding: 3px;
                    color: rgb(191, 191, 191);
                    border-radius:6px 6px;
                    border: 2px solid #3f3f3f;
                    font-size:22px;
                }
                
                QLabel{

                    font-size:16px;
                    color: rgb(191, 191, 191);
                    background-color: transparent;
                }
                
                QPushButton {
                    border:1px solid  rgba(79, 79, 79,0.5) ;
                    border-radius: 6px;	
                    background-color: rgb(79, 79, 79);
                    color: rgb(191, 191, 191);
                    font-size:14px;	
                }
                
                QPushButton:hover {
                    background-color: rgba(36, 104, 149,0.5);
                    border:1px solid rgb(56, 170, 202);
                }
                
                QPushButton:pressed {
                    background-color: rgba(36, 104, 149,0.2);
                    border:1px solid rgb(56, 170, 202);
                }
                
                
                QPushButton:default {
                    border-color: navy; /* make the default button prominent */
                }
                
                QGroupBox{
                    background-color: rgb(48, 48, 48);
                }
                
                QLineEdit{
                    border:none;
                    background-color: rgb(63, 63, 63);
                    font-style: normal;
                    font-weight: normal;
                    font-size: 15px;
                    line-height: 14px;
                    border-radius:10px;
                    color: rgb(191, 191, 191);
                    padding-left:5px;
                } 
                
                QLineEdit:hover{
                    background-color: rgb(68, 68, 68);
                }
                """)
        self.plotting_frame.setStyleSheet("border: 2px solid #3f3f3f;"
                                          "border-radius:6px;")

    def set_features(self):
        """
        set the features and appearance of application's elements
        """
        self.setObjectName("self")
        self.resize(1024, 720)
        self.central_widget.setObjectName("central_widget")

        self.central_widget_grid.setObjectName("central_widget_grid")
        self.main_holder.setObjectName("main_holder")

        self.main_holder.setFrameShape(QFrame.StyledPanel)
        self.main_holder.setFrameShadow(QFrame.Raised)
        self.main_holder_grid.setObjectName("main_holder_grid")
        self.plotting_frame.setObjectName("plotting_frame")

        self.plotting_frame.setFrameShape(QFrame.StyledPanel)
        self.plotting_frame.setFrameShadow(QFrame.Raised)
        self.plotting_frame_grid.setObjectName("plotting_frame_grid")
        self.plotting_frame_grid.addWidget(self.display_function_plot)

        self.main_holder_grid.addWidget(self.plotting_frame, 0, 1, 1, 1)

        self.inputs_group_box.setObjectName("inputs_group_box")
        self.inputs_group_box_grid.setObjectName("inputs_group_box_grid")
        self.inputs_group_box_grid.setHorizontalSpacing(18)
        self.inputs_group_box_grid.setVerticalSpacing(22)
        self.inputs_group_box_grid.setContentsMargins(-1, 33, -1, -1)
        self.plot_button.setObjectName("plot_button")
        self.plot_button.setMinimumSize(QSize(108, 25))

        self.inputs_group_box_grid.addWidget(self.plot_button, 1, 0, 1, 1)

        self.inputs_grid.setSpacing(6)
        self.inputs_grid.setObjectName("inputs_grid")
        self.labels_layout.setObjectName("labels_layout")
        self.function_label.setObjectName("function_label")

        self.labels_layout.addWidget(self.function_label)

        self.maximum_label.setObjectName("maximum_label")

        self.labels_layout.addWidget(self.maximum_label)

        self.minimum_label.setObjectName("minimum_label")

        self.labels_layout.addWidget(self.minimum_label)

        self.inputs_grid.addLayout(self.labels_layout, 0, 0, 1, 1)

        self.inputs_layout.setSpacing(16)
        self.inputs_layout.setObjectName("inputs_layout")
        self.function_input.setObjectName("function_input")
        self.function_input.setMinimumSize(QSize(0, 30))
        self.function_input.setAlignment(Qt.AlignJustify | Qt.AlignVCenter)

        self.inputs_layout.addWidget(self.function_input)

        self.minimum_input.setObjectName("minimum_input")
        self.minimum_input.setMinimumSize(QSize(0, 30))
        self.minimum_input.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.inputs_layout.addWidget(self.minimum_input)

        self.maximum_input.setObjectName("maximum_input")
        self.maximum_input.setMinimumSize(QSize(0, 30))
        self.maximum_input.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.inputs_layout.addWidget(self.maximum_input)

        self.inputs_grid.addLayout(self.inputs_layout, 0, 1, 1, 1)

        self.inputs_group_box_grid.addLayout(self.inputs_grid, 0, 0, 1, 1)

        self.inputs_group_box_grid.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.main_holder_grid.addWidget(self.inputs_group_box, 0, 0, 1, 1)

        self.main_holder_grid.setColumnStretch(0, 1)
        self.main_holder_grid.setColumnStretch(1, 2)

        self.central_widget_grid.addWidget(self.main_holder, 0, 0, 1, 1)

        self.setCentralWidget(self.central_widget)

        QMetaObject.connectSlotsByName(self)

    def set_text(self):
        """
        set visual text in the app
        """
        self.setWindowTitle(QCoreApplication.translate("self", "Function plotter", None))
        self.inputs_group_box.setTitle(QCoreApplication.translate("self", "Inputs panel", None))
        self.plot_button.setText(QCoreApplication.translate("self", "Plot Function", None))
        self.function_label.setText(QCoreApplication.translate("self", "Function:", None))
        self.maximum_label.setText(QCoreApplication.translate("self", "minimum:", None))
        self.minimum_label.setText(QCoreApplication.translate("self", "maximum:", None))
        self.function_input.setPlaceholderText(QCoreApplication.translate("self", "Enter a Function to plot", None))
        self.minimum_input.setPlaceholderText(QCoreApplication.translate("self", "Value to start from", None))
        self.maximum_input.setPlaceholderText(QCoreApplication.translate("self", "Value to end at", None))

    def set_actions(self):
        """
        set actions done by elements like( buttons, QLineEdit )
        """
        self.plot_button.clicked.connect(lambda: self.get_values())
        self.function_input.textEdited.connect(lambda: refactor_style(self.function_input))
        self.minimum_input.textEdited.connect(lambda: refactor_style(self.minimum_input))
        self.maximum_input.textEdited.connect(lambda: refactor_style(self.maximum_input))

    def get_values(self):
        """
        accepts data from input fields and
        """
        # if input fields has data (not empty)
        if self.function_input.text() and self.maximum_input.text() and self.minimum_input.text():
            # try to get data that represent the function and replace any hat (^) symbol with double asterisk ( ** )
            try:
                operation = self.function_input.text().replace('^', '**')

            except:
                # other than this the (unexpected input) will raise exception
                validate_input(self.function_input, massage='Wrong Input')

            # try to get data that represent the start of calculations and convert it into float
            # other than this the (unexpected input) will raise exception
            try:
                start_value = float(self.minimum_input.text())
            except:
                # set default value to 0
                start_value = 0
                validate_input(self.minimum_input, massage='Wrong Input')

            # try to get data that represent the end of calculations and convert it into float
            # other than this the (unexpected input) will raise exception
            try:
                end_value = float(self.maximum_input.text())
            except:
                # set default value to 0
                end_value = 0
                validate_input(self.maximum_input, massage='Wrong Input')

            try:
                # different step in ranges to keep plotting nice and smooth
                if 0 < abs(start_value - end_value) <= 10:

                    x_values = [x for x in np.arange(start_value, end_value, step=0.01)]

                elif 10 < abs(start_value - end_value) <= 100:

                    x_values = [x for x in np.arange(start_value, end_value, step=0.5)]

                else:
                    x_values = [x for x in np.arange(start_value, end_value, step=1)]

                y_values = []

                for x in x_values:
                    # to handle this special case of (Zero Division) negative power and
                    # data range from negative to positive ex: x^-1 , start: -50, end: -50
                    if x == 0 and "^-" in operation:
                        x_values[x_values.index(x)] = 0.0001

                    # evaluate the expression and get result of y
                    y_values.append(eval(operation))
            except:
                # in case the operation is wrong or not valid
                validate_input(self.function_input, massage='correct format: num*x^n')

            if x_values and y_values:
                # plot the points in x_values, y_values
                self.plot_values(x_values, y_values)

        else:
            # raise exception if any field is missing
            [validate_input(object_name) for object_name
             in [self.function_input, self.minimum_input, self.maximum_input]
             if not object_name.text()]

    def plot_values(self, x_values, y_values):
        """
        plot values on x , y
        """
        # clear any graphs on the figure
        self.display_function_plot.ax.clear()
        # restyle the figure
        self.display_function_plot.set_style()
        # plot function values on x, y
        self.display_function_plot.ax.plot(x_values, y_values, color='#08F7FE', linewidth=2, )
        # redraw the figure
        self.display_function_plot.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    home_page = FunctionPlotter()
    home_page.show()

    sys.exit(app.exec_())
