
/*
 * Copyright 2012 Google Inc.
 *
 * Use of this source code is governed by a BSD-style license that can be
 * found in the LICENSE file.
 */


#include "SkSettingsWidget.h"
#include <iostream>
#include <math.h>

// TODO(chudy): See if the layout can't be attached to the frame post construction.
SkSettingsWidget::SkSettingsWidget() : QFrame()
{
    this->setLayout(&fVerticalLayout);
    this->setFrameStyle(QFrame::Panel);
    // Vertical Layout is the alignment inside of the main frame.
    fVerticalLayout.setAlignment(Qt::AlignTop);

    // Visualizations toggles.
    fVisualizationsGroup.setTitle("Visualizations");
    fVisibilityFilterCheckBox.setText("Visibility Filter");
    fVisualizationsLayout.addWidget(&fVisibilityFilterCheckBox);
    fMegaVizCheckBox.setText("Mega Viz");
    fVisualizationsLayout.addWidget(&fMegaVizCheckBox);
    fPathOpsCheckBox.setText("PathOps ");
    fVisualizationsLayout.addWidget(&fPathOpsCheckBox);
    fVisualizationsGroup.setLayout(&fVisualizationsLayout);
    connect(&fVisibilityFilterCheckBox, SIGNAL(toggled(bool)), this,
            SIGNAL(visualizationsChanged()));
    connect(&fMegaVizCheckBox, SIGNAL(toggled(bool)), this, SIGNAL(visualizationsChanged()));
    connect(&fPathOpsCheckBox, SIGNAL(toggled(bool)), this, SIGNAL(visualizationsChanged()));

    fVerticalLayout.addRow(&fVisualizationsGroup);

    // Raster toggles.
    fRasterGroup.setTitle("Raster");
    fRasterGroup.setCheckable(true);
    fOverdrawVizCheckBox.setText("Overdraw Viz");
    fRasterLayout.addWidget(&fOverdrawVizCheckBox);
    fRasterGroup.setLayout(&fRasterLayout);
    fVerticalLayout.addRow(&fRasterGroup);

    connect(&fRasterGroup, SIGNAL(toggled(bool)), this, SIGNAL(rasterSettingsChanged()));
    connect(&fOverdrawVizCheckBox, SIGNAL(toggled(bool)), this, SIGNAL(rasterSettingsChanged()));

#if SK_SUPPORT_GPU
    fGLGroup.setTitle("OpenGL");
    fGLGroup.setCheckable(true);
    fGLGroup.setChecked(false);
    fGLMSAACombo.addItem("Off", QVariant(0));
    fGLMSAACombo.addItem("4", QVariant(4));
    fGLMSAACombo.addItem("16", QVariant(16));
    fGLLayout.addRow("MSAA",  &fGLMSAACombo);
    fGLGroup.setLayout(&fGLLayout);

    connect(&fGLGroup, SIGNAL(toggled(bool)), this,
            SIGNAL(glSettingsChanged()));
    connect(&fGLMSAACombo, SIGNAL(activated(int)), this,
            SIGNAL(glSettingsChanged()));

    fVerticalLayout.addRow(&fGLGroup);
#endif

    fFilterCombo.addItem("As encoded", QVariant(SkPaint::kNone_FilterLevel));
    fFilterCombo.addItem("None", QVariant(SkPaint::kNone_FilterLevel));
    fFilterCombo.addItem("Low", QVariant(SkPaint::kLow_FilterLevel));
    fFilterCombo.addItem("Medium", QVariant(SkPaint::kMedium_FilterLevel));
    fFilterCombo.addItem("High", QVariant(SkPaint::kHigh_FilterLevel));
    connect(&fFilterCombo, SIGNAL(activated(int)), this, SIGNAL(texFilterSettingsChanged()));

    fVerticalLayout.addRow("Filtering", &fFilterCombo);
    this->setDisabled(true);
}

