import {select,
        arc, 
        csv,
        scaleLinear,
        max,
        scalePoint,
        scaleBand,
        axisLeft,
        format,
        axisBottom,
        extent} from 'd3';


        const svg = select('svg');


        //  This is Java script so we can do what we want!!! :)
        const width = +svg.attr('width');
        const height = +svg.attr('height');

        const g = svg.append('g')
        	.attr('transform',`translate(${ width/2 },${ height/2 })`);


        const circle = g.append('circle')
        	.attr('r',height/2)
        	.attr('fill','yellow')
        	.attr('stroke','black');

        const eyeR = 40;
        const eyeSpace = 80;
        const eyeOffset = 50;
        const eveBrow = -110;

        const eyesG = g.append('g')
        	.attr('transform',`translate(0,${-eyeOffset})`);

        const rightEye = eyesG.append('circle')
        	.attr('r',eyeR)
        	.attr('cx', eyeSpace);

        const leftEye = eyesG.append('circle')
        	.attr('r',eyeR)
        	.attr('cx', - eyeSpace);


        const eyesbrowG = g.append('g')
        	.attr('transform',`translate(0,0)`);
        	//.transition()

        eyesbrowG
        	.transition().duration(1000)
        	.attr('transform',`translate(0,-100)`)
        	.transition().duration(1000)
        	.attr('transform',`translate(0,0)`);


        const eyeBrow_1 = eyesbrowG.append('rect')
        	.attr('x',  eyeSpace -35 )
        	.attr('y', eveBrow)
        	.attr('width', 70)
        	.attr('height',15);


        const eyeBrow_2 = eyesbrowG.append('rect')
        	.attr('x', - eyeSpace - 35 )
        	.attr('y', eveBrow)
        	.attr('width', 70)
        	.attr('height',15);
        	//.transition().duration(2000)
        	//	.attr('y', eveBrow -50   );

        const mouth = g.append('path')
        	.attr('d',arc() ({
                innerRadius: 150,
            		outerRadius: 170,
            		startAngle:Math.PI / 2,
            	  endAngle:Math.PI * 3/2
                }));
