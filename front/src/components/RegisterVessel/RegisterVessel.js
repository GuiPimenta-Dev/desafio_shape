import React, { useContext, useState } from "react";
import { Button, Card, Form } from "react-bootstrap";
import AppContext from "../../context/AppContext";

function RegisterVessel() {
  const [vesselCode, setVesselCode] = useState("");
  const appContext = useContext(AppContext);
  const { handleRegisterVessel } = appContext;

  const handleRegisterVesselButton = () => {
    if (vesselCode) {
      handleRegisterVessel(vesselCode);
      setVesselCode("");
    }
  };

  const handleInput = (e) => {
    setVesselCode(e.target.value);
  };

  return (
    <Card className="p-3 mt-3">
      <Form.Group controlId="formBasicEmail">
        <Form.Label>Register a new Vessel:</Form.Label>
        <Form.Control
          onChange={handleInput}
          value={vesselCode}
          type="text"
          placeholder="Vessel Code"
        />
      </Form.Group>
      <Button onClick={handleRegisterVesselButton} variant="info">
        Register
      </Button>
    </Card>
  );
}
export default RegisterVessel;
