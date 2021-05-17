import React, { useContext, useState } from "react";
import { Button, Card, Form, ListGroup } from "react-bootstrap";
import AppContext from "../../context/AppContext";

function SetToInactive() {
  const appContext = useContext(AppContext);
  const { handleSetToInactive } = appContext;
  const [equipmentCode, setEquipmentCode] = useState("");
  const [equipmentCodes, setEquipmentCodes] = useState([]);

  const handleSetToInactiveButton = () => {
    if (equipmentCodes && equipmentCodes.length) {
      handleSetToInactive(equipmentCodes);
      setEquipmentCodes([]);
    }
  };

  const handleInput = (e) => {
    setEquipmentCode(e.target.value);
  };

  const addEquipment = (code) => {
    if (code) {
      setEquipmentCodes((list) => [...list, code]);
      setEquipmentCode("");
    }
  };

  const removeEquipment = (code) => {
    setEquipmentCodes((list) => list.filter((item) => item != code));
  };

  return (
    <Form>
      <Card className="p-3 mt-3 flex-row">
        <div className="col-6">
          <Form.Label>Set a list of Equipments to inactive:</Form.Label>
          <Form.Control
            onChange={handleInput}
            value={equipmentCode}
            className="mb-2"
            type="text"
            placeholder="Equipment Code"
          />
          <div className="d-flex">
            <Button
              onClick={() => addEquipment(equipmentCode)}
              variant="info"
              className="w-100 mr-1"
            >
              Add to list
            </Button>
            <Button
              onClick={handleSetToInactiveButton}
              variant="info"
              className="w-100 ml-1"
            >
              Invert Status
            </Button>
          </div>
        </div>
        <div className="col-6">
          <ListGroup variant="flush" className="box2 overflow-auto">
            {equipmentCodes.map((code) => (
              <ListGroup.Item
                key={code}
                className="d-flex justify-content-between align-items-center"
              >
                <span>{code}</span>
                <Button
                  onClick={() => removeEquipment(code)}
                  variant="danger"
                  size="sm"
                >
                  Remove
                </Button>
              </ListGroup.Item>
            ))}
          </ListGroup>
        </div>
      </Card>
    </Form>
  );
}
export default SetToInactive;
