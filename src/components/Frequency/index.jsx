/* eslint-disable react/prop-types */
import React from 'react'

export default function Frequency({ mode, setMode }) {
  return (
    <div className='mt-12 ml-72 flex gap-4 z-50'>
      {['daily', 'weekly', 'viral'].map((i) => (
        <p
          onClick={() => setMode(i)}
          key={i}
          className={`p-2 px-4 text-xl border rounded rounded-xl p-2 text-center duration-150 border-blue-500 select-none shadow hover:scale-110 hover:shadow-xl ${
            mode === i ? 'font-bold bg-blue-500 text-white' : ''
          }`}
        >
          {i}
        </p>
      ))}
    </div>
  )
}
