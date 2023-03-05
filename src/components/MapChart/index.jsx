/* eslint-disable react/prop-types */
/* eslint-disable no-unused-vars */
import React, { useEffect, useState, memo } from 'react'
import { csv } from 'd3-fetch'
import { scaleLinear } from 'd3-scale'
import { ComposableMap, Geographies, Geography, Sphere, Graticule } from 'react-simple-maps'
import { Tooltip } from 'react-tooltip'

const geoUrl = '/features.json'

const redColorScale = scaleLinear().domain([0.0, 1.0]).range(['#adff2f', '#21421e'])

// eslint-disable-next-line react/prop-types
const MapChart = ({ countryData, setActiveCountry }) => {
  console.log(countryData)
  return (
    <ComposableMap
      projectionConfig={{
        rotate: [-10, 0, 0],
        scale: 147
      }}
    >
      <Sphere stroke='#E4E5E6' strokeWidth={0.5} />
      <Graticule stroke='#E4E5E6' strokeWidth={0.5} />
      {countryData.length > 0 && (
        <Geographies geography={geoUrl}>
          {({ geographies }) =>
            geographies.map((geo) => {
              let country = ['', ' ']
              try {
                country = countryData.find((s) => s[0] === geo.properties.name)
              } catch (err) {
                console.log(err)
              }
              return (
                <Geography
                  key={geo.rsmKey}
                  geography={geo}
                  fill={country ? redColorScale(country[1]) : '#5A5A5A'}
                  onMouseLeave={() => setActiveCountry(['', ''])}
                  onMouseEnter={() => {
                    let country = countryData.find((s) => s[0] === geo.properties.name)
                    setActiveCountry(country ? country : [geo.properties.name, 0])
                    console.log(`${geo.properties.name}`)
                  }}
                  // onMouseLeave={() => {
                  //   setTooltipContent('hello world')
                  // }}
                  style={{
                    hover: {
                      fill: '#FFBF00',
                      outline: 'none'
                    }
                    // pressed: {
                    //   fill: '#E42',
                    //   outline: 'none'
                    // }
                  }}
                />
              )
            })
          }
        </Geographies>
      )}
    </ComposableMap>
  )
}

export default memo(MapChart)
