
"use strict";

let SubmitTray = require('./SubmitTray.js')
let VacuumGripperControl = require('./VacuumGripperControl.js')
let AGVControl = require('./AGVControl.js')
let ConveyorBeltControl = require('./ConveyorBeltControl.js')
let PopulationControl = require('./PopulationControl.js')
let GetMaterialLocations = require('./GetMaterialLocations.js')

module.exports = {
  SubmitTray: SubmitTray,
  VacuumGripperControl: VacuumGripperControl,
  AGVControl: AGVControl,
  ConveyorBeltControl: ConveyorBeltControl,
  PopulationControl: PopulationControl,
  GetMaterialLocations: GetMaterialLocations,
};
