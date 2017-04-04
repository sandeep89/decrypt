import { expect } from 'chai';

import React from 'react';
import ReactShallowRenderer from 'react-addons-test-utils';

import Decrypt from '../../src/js/components/decrypt.jsx';

describe('Decrypt component', function () {
  before(() => {
    let shallowRenderer = ReactShallowRenderer.createRenderer();
    shallowRenderer.render(
      <Decrypt />
    );
    this.result = shallowRenderer.getRenderOutput();
  });

  it('renders a <div>', () => {
    expect(this.result.type).to.equal('div');
  });
});
