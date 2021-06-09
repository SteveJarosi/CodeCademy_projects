import React from 'react';
import ReactDOM from 'react-dom';
import { CopyCat } from '../components/CopyCat'

class CopyCatContainer extends React.Component {
    constructor(props) {
        super(props);
        this.handleChange = this.handleChange.bind(this);

        this.state = {
            copying: true,
            input: ''
        };

        this.toggleTape = this.toggleTape.bind(this);
    }

    handleChange(e) {
        this.setState({ input: e.target.value });
    }

    toggleTape() {
        this.setState({ copying: !this.state.copying })
    }

    render() {
        const copying = this.state.copying;
        const toggleTape = this.toggleTape;
        const onChange = this.handleChange;
        const value = this.state.input;


        return <CopyCat name={Math.random() > 0.5 ? 'Jim' : ''} onChange={onChange} value={value} copying={copying} toggleTape={toggleTape} />;
    };
};


ReactDOM.render(<CopyCatContainer />, document.getElementById('app'));