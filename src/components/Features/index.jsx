/* eslint-disable react/prop-types */
/* eslint-disable no-unused-vars */
import React, { useEffect, useState } from 'react'
import './index.css'

const labels = {
  acousticness: 'Acousticness',
  danceability: 'Danceability',
  energy: 'Energy',
  instrumentalness: 'Instrumentalness',
  key: '',
  loudness: 'Loudness',
  tempo: 'Tempo',
  valence: 'Positivity',
  mode: 'Happiness'
}

const tooltips = {
  acousticness:
    'A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.',
  danceability:
    'Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.',
  energy:
    'Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.',
  instrumentalness:
    'Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.',
  key: '',
  loudness:
    'The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typically range between -60 and 0 db.',
  tempo:
    'The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.',
  valence:
    'A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).',
  mode: 'Indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0.'
}

const Checkboxes = ({ mode, setMapData }) => {
  const [checkboxes, setCheckboxes] = useState({
    acousticness: false,
    danceability: false,
    energy: false,
    instrumentalness: false,
    loudness: false,
    mode: false,
    tempo: false,
    valence: false
  })

  const handleCheckboxChange = (e) => {
    setCheckboxes({ ...checkboxes, [e.target.name]: e.target.checked })
  }

  const getData = async () => {
    let filteredFeautures = Object.entries(checkboxes)
      .filter(([key, value]) => value === true)
      .map(([key, value]) => key)
    filteredFeautures = filteredFeautures.join(',')
    const apiUrl = `http://10.126.117.2:8000/api/country/?mode=${mode}&features=${filteredFeautures}`

    console.log(filteredFeautures)
    fetch(apiUrl, {
      method: 'GET'
    })
      .then((response) => response.json())
      .then((data) => {
        setMapData(data)
      })
      .catch((error) => {
        // handle errors here
      })
  }

  useEffect(() => {
    getData()
  }, [checkboxes, mode])

  return (
    <div className='checkboxes-container flex flex-col items-center gap-12'>
      <h2 className='text-3xl font-semibold'>Choose your features:</h2>
      <div className='checkboxes flex flex-col items-center gap-1'>
        {Object.keys(checkboxes).map((key) => (
          <p
            onClick={(e) => {
              setCheckboxes({ ...checkboxes, [key]: !checkboxes[key] })
            }}
            key={key}
            className={`group relative w-full text-center hover:translate-x-3 text-center checkbox-container select-none p-2 border border-green-500 rounded hover:bg-green-500 hover:text-white duration-150 shadow-lg ${
              checkboxes[key] ? 'text-green-500 translate-x-3' : ''
            }`}
          >
            {labels[key]}
            <a
              href='#'
              className='w-48 hidden p-1 px-2 border border-slate-800 bg-slate-700/75 text-xs  absolute group-hover:block -top-12 -left-[250px] text-white transition duration-150 ease-in-out hover:text-primary-600 focus:text-primary-600 active:text-primary-700 dark:text-primary-400 dark:hover:text-primary-500 dark:focus:text-primary-500 dark:active:text-primary-600 rounded'
            >
              {tooltips[key]}
            </a>
          </p>
        ))}
      </div>
      <button
        type='submit'
        onClick={getData}
        className='hidden w-full text-lg font-semibold p-2 border hover:bg-white hover:text-black rounded-lg duration-150 shadow-xl'
      >
        Render
      </button>
    </div>
  )
}

export default Checkboxes
