import React, { useState } from "react";
import axios from "axios";
import AppContext from "./AppContext";

const AppState = (props) => {
  const apiUrl = "https://shapechallenge.herokuapp.com";
  const [equipmentsList, setEquipmentsList] = useState([]);
  const [equipObject, setEquipObject] = useState({
    equipCode: "",
    vesselCode: "",
    equipName: "",
    location: "",
  });

  const [showToast, setShowToast] = useState(false);
  const [toastMessage, setToastMessage] = useState("");
  const [toastStatus, setToastStatus] = useState("success");

  const handleFind = async (vesselCode) => {
    try {
      const res = await axios.get(`${apiUrl}/vessel/${vesselCode}`);

      const {message, data} = res.data
      const finalMessage = message ? message : "There are no equipments in this vessel"
      setToastMessage(finalMessage);
      if(data instanceof Array){
        setEquipmentsList(data);
      }else {
        setEquipmentsList([]);
      }
      setToastStatus((res.status+"")[0] === "2" ? "success" : "danger");
    } catch (e) {
      setToastMessage(e.message);
      setToastStatus("danger");
    }
    setShowToast(true);
  };

  const handleSetToInactive = async (equipmentCodes) => {
    try {
      const res = await axios.get(
        `${apiUrl}/status?code=${equipmentCodes.join()}`
      );
      setToastMessage("Equipments status were reversed");
      setToastStatus((res.status+"")[0] === "2" ? "success" : "danger");
    } catch (e) {
      setToastMessage(e.message);
      setToastStatus("danger");
    }
    setShowToast(true);
  };

  const handleRegisterVessel = async (vesselCode) => {
    try {
      const formData = new FormData();
      formData.append("code", vesselCode);
      const config = {
        headers: {
          "content-type": "multipart/form-data",
        },
      };

      const res = await axios.post(`${apiUrl}/vessels`, formData, config);
      const {message} = res.data
      setToastMessage(message);
      setToastStatus((res.status+"")[0] === "2" ? "success" : "danger");
    } catch (e) {
      setToastMessage(e.message);
      setToastStatus("danger");
    }
    setShowToast(true);
  };

  const handleRegisterEquipment = async () => {
    try {
      const formData = new FormData();

      formData.append("code", equipObject.equipCode);
      formData.append("location", equipObject.location);
      formData.append("name", equipObject.equipName);
      const config = {
        headers: {
          "content-type": "multipart/form-data",
        },
      };

      const res = await axios.post(`${apiUrl}/equipment/${equipObject.vesselCode}`, formData, config);

      const {message} = res.data
      setToastMessage(message);
      setToastStatus((res.status+"")[0] === "2" ? "success" : "danger");
    } catch (e) {
      setToastMessage(e.message);
      setToastStatus("danger");
    }
    setShowToast(true);
  };

  return (
    <AppContext.Provider
      value={{
        handleFind,
        equipmentsList,
        handleSetToInactive,
        handleRegisterVessel,
        handleRegisterEquipment,
        showToast,
        setShowToast,
        toastMessage,
        toastStatus,
        equipObject,
        setEquipObject,
      }}
    >
      {props.children}
    </AppContext.Provider>
  );
};

export default AppState;
