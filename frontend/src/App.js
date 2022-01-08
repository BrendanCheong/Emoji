import { useState } from "react"
import axios from "axios"
import './App.css';
import laugh_cry from "./images/laugh_cry.png"
import eggplant from "./images/eggplant.png"
import peach from "./images/peach.png"
import drip from "./images/drip.png"

function App() {

  const [currentDoi, setCurrentDoi] = useState("");
  const [waiting, setWaiting] = useState(false);
  const [error, setError] = useState(false);
  const [emojiText, setEmojiText] = useState("");

  const handleChange = (e) => {
    setCurrentDoi(e.target.value)
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const payload = {
      doi: currentDoi,
    };

    try {
      setWaiting(true)
      const response = await axios.post("localhost:8080/emoji", payload);
      const data = response.data.msg;
      setEmojiText(data);
      setWaiting(false);
    } catch(e) {
      setError(true);
      console.error(e);
    }

  }

  return (
    <div className="w-screen h-screen">
        <div className="relative w-full h-full bg-center bg-cover" style={{"backgroundImage": "url('https://img.sci-hub.shop/scihub/top-back.jpg')"}}>
          <form
          className="w-[172px] h-[336px] bg-cover bg-center top-56 absolute left-28 z-0"
          style={{"backgroundImage": "url('https://img.sci-hub.shop/scihub/raven_1.png')"}}
          onSubmit={(e) => handleSubmit(e)}>
            <img className="absolute z-50 w-26 h-26 -top-16 left-8" alt="laugh cry emoji" src={laugh_cry}></img>
            <div
            className="w-[675px] h-[160px] bg-cover bg-center top-32 absolute left-56 z-0"
            style={{"backgroundImage": "url('https://img.sci-hub.shop/scihub/logo_en.png')"}}
            >
              <input className="absolute w-full px-3 py-2 leading-tight text-gray-700 border rounded shadow appearance-none -bottom-20 left-10 focus:outline-none focus:shadow-outline" id="username" type="text" placeholder="Enter Doi here" value={currentDoi}
              onChange={(e) => handleChange(e)}></input>
              <button className="absolute px-5 py-2 text-white bg-red-500 -bottom-20 -right-44 rounded-xl hover:bg-red-600" type="submit"
              >Search</button>
            </div>
          </form>
          <img className="w-56 h-56 z-50 absolute -rotate-45 left-[24rem] opacity-50" src={eggplant} alt="eggplant emoji"></img>
          <img className="w-56 h-56 z-50 absolute -rotate-12 right-[56rem] opacity-50 top-24" src={peach} alt="peach emoji"></img>
          <img className="w-56 h-56 z-50 absolute -rotate-12 right-[24rem] opacity-75 top-56" src={drip} alt="drip emoji"></img>
          <img className="w-56 h-56 z-50 absolute -rotate-90 left-[24rem] opacity-50 bottom-10" src={eggplant} alt="eggplant emoji"></img>
          <img className="w-56 h-56 z-50 absolute -rotate-12 right-[12rem] opacity-50 bottom-24" src={peach} alt="peach emoji"></img>
          <img className="w-56 h-56 z-50 absolute -rotate-12 right-[24rem] opacity-75 top-56" src={drip} alt="drip emoji"></img>
          {/* <img className="absolute z-50 w-56 h-56 opacity-50 -rotate-12" src={peach} alt="peach emoji"> </img> */}
          <p className="absolute bottom-0 text-3xl">{emojiText}</p>
          {waiting ? <>
            <div>
              <p className="absolute bottom-0 text-6xl text-orange-600"> LOADING</p>
            </div>
          </> : <></>}
          {
            error
              ? <>
                <div>
                  <p className="absolute bottom-0 text-6xl text-red-600">
                    ERROR
                  </p>
                </div>
              </>
              : <></>
          }
      </div>
        
    </div>
  );
}

export default App;
