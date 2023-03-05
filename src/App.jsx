import React, { useEffect, useState } from 'react'
import ReactDOM from 'react-dom'

import MapChart from './components/MapChart'
import Features from './components/Features'
import 'react-tooltip/dist/react-tooltip.css'
import './App.css'
import GreyRectangleBar from './components/TopBar'
import Frequency from './components/Frequency'

export default function App() {
  const [mode, setMode] = useState('daily')
  const [mapData, setMapData] = useState([])
  const [activeCountry, setActiveCountry] = useState(['', ' '])

  useEffect(() => {
    console.log()
  }, [])

  return (
    <div className='bg-[#191414]/80 text-[#fff] h-screen'>
      <GreyRectangleBar />
      <div className='relative flex flex-col justify-center'>
        <div className='absolute top-0 right-1/3 text-center flex justify-center items-center gap-8'>
          <Frequency setMode={setMode} mode={mode} />
        </div>
        <div className='flex gap-4 items-center justify-center'>
          <Features mode={mode} setMapData={setMapData} />
          <div className='relative w-[60%]'>
            <MapChart countryData={mapData} setActiveCountry={setActiveCountry} />
            <div className='absolute text-center flex flex-col left-[475px] bottom-10'>
              <p className='text-5xl'>{activeCountry[0]}</p>
              <p className='text-3xl'>{activeCountry[1] ? Math.round(activeCountry[1] * 1000) / 1000 : ''}</p>
            </div>
          </div>
        </div>
      </div>
      <div className='hidden mt-auto bg-gray-700 h-30'>
        <p>Footer</p>
      </div>
    </div>
  )
}

const rootElement = document.getElementById('root')
ReactDOM.render(<App />, rootElement)
