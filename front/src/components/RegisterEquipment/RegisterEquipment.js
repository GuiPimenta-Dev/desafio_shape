import React, { useContext, useState } from "react";
import { Button, Card, Form } from "react-bootstrap";
import AppContext from "../../context/AppContext";

function RegisterEquipment() {
  const appContext = useContext(AppContext);
  const { handleRegisterEquipment, equipObject, setEquipObject } = appContext;

  const handleRegisterEquipmentButton = () => {
    handleRegisterEquipment(equipObject);
    setEquipObject({
      equipCode: "",
      vesselCode: "",
      equipName: "",
      location: "",
    });
  };

  const handleInput = (input) => (e) => {
    setEquipObject((obj) => ({ ...obj, [input]: e.target.value }));
  };

  return (
    <Card className="p-3 mt-3">
      <Form.Group controlId="formBasicPassword">
        <Form.Label>Register an Equipment in a Vessel:</Form.Label>
        <Form.Control
          onChange={handleInput("vesselCode")}
          value={equipObject.vesselCode}
          className="mb-2"
          type="text"
          placeholder="Vessel Code"
        />
        <Form.Control
          onChange={handleInput("equipCode")}
          value={equipObject.equipCode}
          className="mb-2"
          type="text"
          placeholder="Equipment Code"
        />
        <Form.Control
          onChange={handleInput("equipName")}
          value={equipObject.equipName}
          className="mb-2"
          type="text"
          placeholder="Equipment Name"
        />
        <Form.Control
          onChange={handleInput("location")}
          value={equipObject.location}
          type="text"
          placeholder="Location"
        />
      </Form.Group>

      <Button onClick={handleRegisterEquipmentButton} variant="info">
        Register
      </Button>
    </Card>
  );
}
export default RegisterEquipment;
