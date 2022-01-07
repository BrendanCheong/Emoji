import './App.css';
import laugh_cry from "./images/laugh_cry.png"
import logo from "./images/logo.png"
import eggplant from "./images/eggplant.png"
import peach from "./images/peach.png"
import drip from "./images/drip.png"

function App() {
  return (
    <div className="w-screen h-screen">
        <div className="bg-cover bg-center w-full h-full relative" style={{"background-image": "url('https://img.sci-hub.shop/scihub/top-back.jpg')"}}>
          <div
          className="w-[172px] h-[336px] bg-cover bg-center top-56 absolute left-28 z-0"
          style={{"background-image": "url('https://img.sci-hub.shop/scihub/raven_1.png')"}}>
            <img className="w-26 h-26 z-50 absolute -top-16 left-8" alt="laugh cry emoji" src={laugh_cry}></img>
            <div
            className="w-[675px] h-[160px] bg-cover bg-center top-32 absolute left-56 z-0"
            style={{"background-image": "url('https://img.sci-hub.shop/scihub/logo_en.png')"}}
            ></div>
          </div>
          <img className="w-56 h-56 z-50 absolute -rotate-45 left-[24rem] opacity-50" src={eggplant} alt="eggplant emoji"></img>
          <img className="w-56 h-56 z-50 absolute -rotate-12 right-[56rem] opacity-50 top-24" src={peach} alt="peach emoji"></img>
          <img className="w-56 h-56 z-50 absolute -rotate-12 right-[24rem] opacity-75 top-56" src={drip} alt="drip emoji"></img>
          <img className="w-56 h-56 z-50 absolute -rotate-90 left-[24rem] opacity-50 bottom-10" src={eggplant} alt="eggplant emoji"></img>
          <img className="w-56 h-56 z-50 absolute -rotate-12 right-[12rem] opacity-50 bottom-24" src={peach} alt="peach emoji"></img>
          <img className="w-56 h-56 z-50 absolute -rotate-12 right-[24rem] opacity-75 top-56" src={drip} alt="drip emoji"></img>
          {/* <img className="w-56 h-56 z-50 absolute -rotate-12 opacity-50" src={peach} alt="peach emoji"> </img> */}
      </div>
    </div>
  );
}

export default App;
